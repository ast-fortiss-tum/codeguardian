// Source: Row 2 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_276.xlsx


// Create temporary file for write
std::string pwdFile(passwdFileName);
std::vector<char> tempFileName(pwdFile.begin(), pwdFile.end());
std::vector<char> fileTemplate = {'_', '_', 'X', 'X', 'X',
                                    'X', 'X', 'X', '\0'};
tempFileName.insert(tempFileName.end(), fileTemplate.begin(),
                    fileTemplate.end());
int fd = mkstemp((char*)tempFileName.data());
if (fd == -1)
{
    log<level::DEBUG>("Error creating temp file");
    return -EIO;
}

std::string strTempFileName(tempFileName.data());
// Open the temp file for writing from provided fd
// By "true", remove it at exit if still there.
// This is needed to cleanup the temp file at exception
phosphor::user::File temp(fd, strTempFileName, "w", true);
if ((temp)() == NULL)
{
    close(fd);
    log<level::DEBUG>("Error creating temp file");
    return -EIO;
}

// Set the file mode as of actual ipmi-pass file.
if (fchmod(fileno((temp)()), st.st_mode) < 0)
{
    log<level::DEBUG>("Error setting fchmod for temp file");
    return -EIO;
}
