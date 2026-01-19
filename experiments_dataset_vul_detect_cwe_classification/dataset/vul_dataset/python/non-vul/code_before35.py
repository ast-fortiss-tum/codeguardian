# Source: Row 116 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx
 
def add(self, image_id, image_file, image_size, connection=None):
    location = self.create_location(image_id)
    if not connection:
        connection = self.get_connection(location)

    self._create_container_if_missing(location.container, connection)

    LOG.debug(_("Adding image object '%(obj_name)s' "
                "to Swift") % dict(obj_name=location.obj))
    try:
        if image_size > 0 and image_size < self.large_object_size:
            # Image size is known, and is less than large_object_size.
            # Send to Swift with regular PUT.
            obj_etag = connection.put_object(location.container,
                                                location.obj, image_file,
                                                content_length=image_size)
        else:
            # Write the image into Swift in chunks.
            chunk_id = 1
            if image_size > 0:
                total_chunks = str(int(
                    math.ceil(float(image_size) /
                                float(self.large_object_chunk_size))))
            else:
                # image_size == 0 is when we don't know the size
                # of the image. This can occur with older clients
                # that don't inspect the payload size.
                LOG.debug(_("Cannot determine image size. Adding as a "
                            "segmented object to Swift."))
                total_chunks = '?'

            checksum = hashlib.md5()
            combined_chunks_size = 0
            while True:
                chunk_size = self.large_object_chunk_size
                if image_size == 0:
                    content_length = None
                else:
                    left = image_size - combined_chunks_size
                    if left == 0:
                        break
                    if chunk_size > left:
                        chunk_size = left
                    content_length = chunk_size

                chunk_name = "%s-%05d" % (location.obj, chunk_id)
                reader = ChunkReader(image_file, checksum, chunk_size)
                chunk_etag = connection.put_object(
                    location.container, chunk_name, reader,
                    content_length=content_length)
                bytes_read = reader.bytes_read
                msg = _("Wrote chunk %(chunk_name)s (%(chunk_id)d/"
                        "%(total_chunks)s) of length %(bytes_read)d "
                        "to Swift returning MD5 of content: "
                        "%(chunk_etag)s")
                LOG.debug(msg % locals())

                if bytes_read == 0:
                    # Delete the last chunk, because it's of zero size.
                    # This will happen if size == 0.
                    LOG.debug(_("Deleting final zero-length chunk"))
                    connection.delete_object(location.container,
                                                chunk_name)
                    break

                chunk_id += 1
                combined_chunks_size += bytes_read

            # In the case we have been given an unknown image size,
            # set the size to the total size of the combined chunks.
            if image_size == 0:
                image_size = combined_chunks_size

            # Now we write the object manifest and return the
            # manifest's etag...
            manifest = "%s/%s" % (location.container, location.obj)
            headers = {'ETag': hashlib.md5("").hexdigest(),
                        'X-Object-Manifest': manifest}

