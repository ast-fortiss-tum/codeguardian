// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0078/char_connect_socket_w32_spawnv_73b.cpp

void func(list<char *> dataList)
{
    char * data = dataList.back();
    {
        char *args[] = {COMMAND_INT_PATH, COMMAND_ARG1, COMMAND_ARG3, NULL};
        /* spawnv - specify the path where the command is located */
        _spawnv(_P_WAIT, COMMAND_INT_PATH, args);
    }
}
