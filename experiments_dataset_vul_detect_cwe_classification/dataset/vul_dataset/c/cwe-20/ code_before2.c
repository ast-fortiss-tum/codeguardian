// Source: Row 10 in ./dataset/CVEfixes/Analysis/results/C/df_c_cwe_20.xlsx

void CIRCNetwork::SetEncoding(const CString& s) {
    m_sEncoding = CZNC::Get().FixupEncoding(s);
    if (GetIRCSock()) {
        GetIRCSock()->SetEncoding(m_sEncoding);
    }
}