// From cwe-snippets, ./snippets_1/non-compliant/Java/0015.java

public String coordinateTransformLatLonToUTM(String coordinates)
                 {
    String utmCoords = null;
    try {
        String latlonCoords = coordinates;
        Runtime rt = Runtime.getRuntime();
        Process exec = rt.exec("cmd.exe /C latlon2utm.exe -" + latlonCoords);
        // process results of coordinate transform
    }
    return utmCoords;
}