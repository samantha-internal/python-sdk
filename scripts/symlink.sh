cd whitehead_sdk/api && for m in ../../whitehead_graphql/common/*.graphql ; do ln -s $m \"${m##*/}\"; done
