// From JSVulnerabilityDataSet, row no. 8900 .

db.incrObjectField('global', 'nextTid', function(err, tid) {
    if (err) {
        return callback(err);
    }

    var slug = utils.slugify(title),
        timestamp = Date.now();

    if (!slug.length) {
        return callback(new Error('[[error:invalid-title]]'));
    }

    slug = tid + '/' + slug;

    var topicData = {
        'tid': tid,
        'uid': uid,
        'cid': cid,
        'mainPid': 0,
        'title': title,
        'slug': slug,
        'timestamp': timestamp,
        'lastposttime': 0,
        'postcount': 0,
        'viewcount': 0,
        'locked': 0,
        'deleted': 0,
        'pinned': 0
    };

    if (data.thumb) {
        topicData.thumb = data.thumb;
    }

    db.setObject('topic:' + tid, topicData, function(err) {
        if (err) {
            return callback(err);
        }

        async.parallel([
            function(next) {
                db.sortedSetsAdd([
                    'topics:tid',
                    'cid:' + cid + ':tids',
                    'cid:' + cid + ':uid:' + uid + ':tids'
                ], timestamp, tid, next);
            },
            function(next) {
                user.addTopicIdToUser(uid, tid, timestamp, next);
            },
            function(next) {
                db.incrObjectField('category:' + cid, 'topic_count', next);
            },
            function(next) {
                db.incrObjectField('global', 'topicCount', next);
            },
            function(next) {
                Topics.createTags(tags, tid, timestamp, next);
            }
        ], function(err) {
            if (err) {
                return callback(err);
            }
            plugins.fireHook('action:topic.save', topicData);
            callback(null, tid);
        });
    });
});

