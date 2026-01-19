// Source: Row 9 in ./dataset/CVEfixes/Analysis/results/Java/df_java_cwe_89.xlsx

@Override
public String getParameterSQL(Object param) {
    if (param == null) {
        return "null";
    }
    if (param instanceof Number) {
        return getNumberParameterSQL((Number) param);
    }
    if (param instanceof Date) {
        return getDateParameterSQL((Date) param);
    }
    return getStringParameterSQL(param.toString());
}


@Override
public String getNumberParameterSQL(Number param) {
    return param.toString();
}

SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.S");

@Override
public String getDateParameterSQL(Date param) {
    // timestamp '2015-08-24 13:14:36.615'
    return "TIMESTAMP '" + dateFormat.format(param) + "'";
}

@Override
public String getStringParameterSQL(String param) {
    // DASHBUILDE-113: SQL Injection on data set lookup filters
    String escapedParam = param.replaceAll("'", "''");
    return "'" + escapedParam + "'";
}
