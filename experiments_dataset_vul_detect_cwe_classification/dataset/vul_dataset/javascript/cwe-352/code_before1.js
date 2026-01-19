// Source: Row 6 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_352.xlsx

function rcmail_zipdownload(mode)
{
    // default .eml download of single message
    if (mode == 'eml') {
        var uid = rcmail.get_single_uid();
        rcmail.goto_url('viewsource', rcmail.params_from_uid(uid, {_save: 1}));
        return;
    }

    // multi-message download, use hidden form to POST selection
    if (rcmail.message_list && rcmail.message_list.get_selection().length > 1) {
        var inputs = [], form = $('#zipdownload-form'),
            post = rcmail.selection_post_data();

        post._mode = mode;
        post._token = rcmail.env.request_token;

        $.each(post, function(k, v) {
            if (typeof v == 'object' && v.length > 1) {
              for (var j=0; j < v.length; j++)
                  inputs.push($('<input>').attr({type: 'hidden', name: k+'[]', value: v[j]}));
            }
            else {
                inputs.push($('<input>').attr({type: 'hidden', name: k, value: v}));
            }
        });

        if (!form.length)
            form = $('<form>').attr({
                    style: 'display: none',
                    method: 'POST',
                    action: '?_task=mail&_action=plugin.zipdownload.messages'
                })
                .appendTo('body');

        form.html('').append(inputs).submit();
    }
}