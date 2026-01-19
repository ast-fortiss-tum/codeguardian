// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0023/wchar_t_file_w32CreateFile_07.cpp

static void func()
{
    wchar_t * data;
    wchar_t dataBuffer[FILENAME_MAX] = BASEPATH;
    data = dataBuffer;
    if(staticFive==5)
    {
        /* FIX: Use a fixed file name */
        wcscat(data, L"file.txt");
    }
    {
        HANDLE hFile;
        hFile = CreateFileW(data,
                            (GENERIC_WRITE|GENERIC_READ),
                            0,
                            NULL,
                            OPEN_ALWAYS,
                            FILE_ATTRIBUTE_NORMAL,
                            NULL);
        if (hFile != INVALID_HANDLE_VALUE)
        {
            CloseHandle(hFile);
        }
    }
}

