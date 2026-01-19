// Source: Row 15 in ./dataset/CVEfixes/Analysis/results/Java/df_java_cwe_20.xlsx

public class Http2HeadersAdaptor implements MultiMap {

  static CharSequence toLowerCase(CharSequence s) {
    StringBuilder buffer = null;
    int len = s.length();
    for (int index = 0; index < len; index++) {
      char c = s.charAt(index);
      if (c >= 'A' && c <= 'Z') {
        if (buffer == null) {
          buffer = new StringBuilder(s);
        }
        buffer.setCharAt(index, (char)(c + ('a' - 'A')));
      }
    }
    if (buffer != null) {
      return buffer.toString();
    } else {
      return s;
    }
  }

  private final Http2Headers headers;
  private Set<String> names;

  public Http2HeadersAdaptor(Http2Headers headers) {

    List<CharSequence> cookies = headers.getAll(HttpHeaderNames.COOKIE);
    if (cookies != null && cookies.size() > 1) {
      // combine the cookie values into 1 header entry.
      // https://tools.ietf.org/html/rfc7540#section-8.1.2.5
      String value = cookies.stream().collect(Collectors.joining("; "));
      headers.set(HttpHeaderNames.COOKIE, value);
    }

    this.headers = headers;
  }

  @Override
  public String get(String name) {
    CharSequence val = headers.get(toLowerCase(name));
    return val != null ? val.toString() : null;
  }

  @Override
  public List<String> getAll(String name) {
    List<CharSequence> all = headers.getAll(toLowerCase(name));
    if (all != null) {
      return new AbstractList<String>() {
        @Override
        public String get(int index) {
          return all.get(index).toString();
        }
        @Override
        public int size() {
          return all.size();
        }
      };
    }
    return null;
  }

  @Override
  public List<Map.Entry<String, String>> entries() {
    return headers.names()
        .stream()
        .map(name -> new AbstractMap.SimpleEntry<>(name.toString(), headers.get(name).toString()))
        .collect(Collectors.toList());
  }

  @Override
  public boolean contains(String name) {
    return headers.contains(toLowerCase(name));
  }

  @Override
  public boolean contains(String name, String value, boolean caseInsensitive) {
    return headers.contains(toLowerCase(name), value, caseInsensitive);
  }

  @Override
  public boolean isEmpty() {
    return headers.isEmpty();
  }

  @Override
  public Set<String> names() {
    if (names == null) {
      names = new AbstractSet<String>() {
        @Override
        public Iterator<String> iterator() {
          Iterator<CharSequence> it = headers.names().iterator();
          return new Iterator<String>() {
            @Override
            public boolean hasNext() {
              return it.hasNext();
            }
            @Override
            public String next() {
              return it.next().toString();
            }
          };
        }
        @Override
        public int size() {
          return headers.size();
        }
      };
    }
    return names;
  }

  @Override
  public MultiMap add(String name, String value) {
    headers.add(toLowerCase(name), value);
    return this;
  }

  @Override
  public MultiMap add(String name, Iterable<String> values) {
    headers.add(toLowerCase(name), values);
    return this;
  }

  @Override
  public MultiMap addAll(MultiMap headers) {
    for (Map.Entry<String, String> entry: headers.entries()) {
      add(entry.getKey(), entry.getValue());
    }
    return this;
  }
