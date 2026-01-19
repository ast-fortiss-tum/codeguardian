// Source: Row 129 in ./dataset/CVEfixes/Analysis/results/C++/df_cpp_all.xlsx

void Messageheader::Parser::checkHeaderspace(unsigned chars) const
{
if (headerdataPtr + chars >= header.rawdata + sizeof(header.rawdata))
{
    header.rawdata[sizeof(header.rawdata) - 1] = '\0';
    throw HttpError(HTTP_REQUEST_ENTITY_TOO_LARGE, "header too large");
}
}