// Source: Row 2 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_22.xlsx

CString CWebSock::GetSkinPath(const CString& sSkinName) {
    const CString sSkin = sSkinName.Replace_n("/", "_").Replace_n(".", "_");

    CString sRet = CZNC::Get().GetZNCPath() + "/webskins/" + sSkin;

    if (!CFile::IsDir(sRet)) {
        sRet = CZNC::Get().GetCurPath() + "/webskins/" + sSkin;

        if (!CFile::IsDir(sRet)) {
            sRet = CString(_SKINDIR_) + "/" + sSkin;
        }
    }

    return sRet + "/";
}