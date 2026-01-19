// Source: Row 154 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_125.xlsx

for (i = 0; i < mapi->count; i++) {
      mapidata = &(mapi->data[i]);
      if (mapi->count > 1) {
        printf("    [%i/%u] ", i, mapi->count);
      } else {
        printf("    ");
      }
      printf("Size: %i", mapidata->size);
      switch (PROP_TYPE(mapi->id)) {
        case PT_SYSTIME:
          MAPISysTimetoDTR(mapidata->data, &thedate);
          printf("    Value: ");
          ddword_tmp = *((DDWORD *)mapidata->data);
          TNEFPrintDate(thedate);
          printf(" [HEX: ");
          for (x = 0; x < sizeof(ddword_tmp); x++) {
            printf(" %02x", (BYTE)mapidata->data[x]);
          }
          printf("] (%llu)\n", ddword_tmp);
          break;
        case PT_LONG:
          printf("    Value: %i\n", *((int*)mapidata->data));