// Source: Row 11 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_20.xlsx

void CIRCNetwork::SetEncoding(const CString& s) {
    m_sEncoding = s;
    if (GetIRCSock()) {
        GetIRCSock()->SetEncoding(s);
    }
}