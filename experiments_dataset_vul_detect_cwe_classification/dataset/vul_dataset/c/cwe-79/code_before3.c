// Source: Row 17 in ./dataset/CVEfixes/Analysis/results/C/df_c_cwe_79.xlsx

rndr_quote(struct buf *ob, const struct buf *text, void *opaque)
{
	if (!text || !text->size)
		return 0;

	BUFPUTSL(ob, "<q>");
	bufput(ob, text->data, text->size);
	BUFPUTSL(ob, "</q>");

	return 1;
}