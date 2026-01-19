// Source: Row 29 in ./dataset/CVEfixes/Analysis/results/Java/df_java_cwe_20.xlsx

private void add0(int h, int i, final CharSequence name, final CharSequence value) {
if (!(name instanceof AsciiString)) {
    HttpUtils.validateHeader(name);
}
if (!(value instanceof AsciiString)) {
    HttpUtils.validateHeader(value);
}
