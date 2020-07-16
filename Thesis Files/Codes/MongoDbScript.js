use users
show collections
db.AprEighth.count()

db.AprEighth.aggregate([{$group:{_id:null,RetweetSum:{$sum:"$Retweet Count"}}}])
db.AprEighth.aggregate([{$group:{_id:null,RetweetCntMax:{$max:"$Retweet Count"}}}])
db.AprEighth.aggregate([{$group:{_id:"$Retweet Count",RetweetCnt:{$sum:1}}},{$group:{_id:null,DistinctRetweetSum:{$sum:"$_id"}}}])

db.AprEighth.aggregate([{$group:{_id:null,FriendsSum:{$sum:"$Friends Count"}}}])
db.AprEighth.aggregate([{$group:{_id:null,FriendsCntMax:{$max:"$Friends Count"}}}])
db.AprEighth.aggregate([{$group:{_id:"$Friends Count",FriendsCnt:{$sum:1}}},{$group:{_id:null,DistinctFiendsSum:{$sum:"$_id"}}}])

db.AprEighth.aggregate([{$group:{_id:null,FollowersSum:{$sum:"$Followers Count"}}}])
db.AprEighth.aggregate([{$group:{_id:null,FollowersCntMax:{$max:"$Followers Count"}}}])
db.AprEighth.aggregate([{$group:{_id:"$Followers Count",FollowersCnt:{$sum:1}}},{$group:{_id:null,DistinctFollowersSum:{$sum:"$_id"}}}])

db.AprEighth.aggregate([{$group:{_id:"$Time Zone",count:{$sum:1}}}])
it
it
it
it
it







