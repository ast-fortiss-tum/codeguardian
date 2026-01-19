// From cwe-snippets, snippets_2/non-compliant/Java/0179.java

final String foldername = request.getParameter("folder");
  IMAPFolder folder = (IMAPFolder) store.getFolder("INBOX");
  folder.doCommand(new IMAPFolder.ProtocolCommand() {
      @Override
      public Object doCommand(IMAPProtocol imapProtocol) throws ProtocolException {
          try {
              imapProtocol.simpleCommand("CREATE " + foldername, null);
          } catch (Exception e) {
              // Handle Exception
          }
          return null;
      }
  });