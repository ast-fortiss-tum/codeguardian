// Source: Row 3 in ./dataset/CVEfixes/Analysis/results/Python/df_java_cwe_434.xlsx

private Component newUploadPanel() {
	Fragment fragment;

	IModel<Collection<FileUpload>> model = new PropertyModel<Collection<FileUpload>>(this, "uploads");
	String acceptedFiles;
	if (isImage)
		acceptedFiles = "image/*";
	else
		acceptedFiles = null;
	
	AttachmentSupport attachmentSupport = markdownEditor.getAttachmentSupport();
	if (attachmentSupport != null) {
		fragment = new Fragment(CONTENT_ID, "uploadAttachmentFrag", this);
		
		Form<?> form = new Form<Void>("form") {

			@Override
			protected void onSubmit() {
				super.onSubmit();
				
				AjaxRequestTarget target = RequestCycle.get().find(AjaxRequestTarget.class);
				String attachmentName;
				FileUpload upload = uploads.iterator().next();
				try (InputStream is = upload.getInputStream()) {
					attachmentName = attachmentSupport.saveAttachment(
							FilenameUtils.sanitizeFilename(upload.getClientFileName()), is);
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
				markdownEditor.insertUrl(target, isImage, 
						attachmentSupport.getAttachmentUrl(attachmentName), UrlUtils.describe(attachmentName), null);
				onClose(target);
			}

			@Override
			protected void onFileUploadException(FileUploadException e, Map<String, Object> model) {
				throw new RuntimeException(e);
			}
			
		};
		form.setMaxSize(Bytes.bytes(attachmentSupport.getAttachmentMaxSize()));
		form.setMultiPart(true);
		form.add(new FencedFeedbackPanel("feedback", form));
		
		int maxFilesize = (int) (attachmentSupport.getAttachmentMaxSize()/1024/1024);
		if (maxFilesize <= 0)
			maxFilesize = 1;
		form.add(new DropzoneField("file", model, acceptedFiles, 1, maxFilesize)
				.setRequired(true).setLabel(Model.of("Attachment")));
		
		form.add(new AjaxButton("insert"){});
		
		fragment.add(form);
	} else {
		fragment = new Fragment(CONTENT_ID, "uploadBlobFrag", this);
		Form<?> form = new Form<Void>("form");
		form.setMultiPart(true);
		form.setFileMaxSize(Bytes.megabytes(Project.MAX_UPLOAD_SIZE));
		add(form);
		
		FencedFeedbackPanel feedback = new FencedFeedbackPanel("feedback", form);
		feedback.setOutputMarkupPlaceholderTag(true);
		form.add(feedback);
			