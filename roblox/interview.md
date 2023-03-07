Roblox Social team DS ，华人小哥说目前就他一人负责整个social，在招人。-baidu 1point3acres
1. sql 求retention 不难
2. 产品：
- How would you measure social on roblox？
- Roblox wants to launch voice feature, how would you measure it?
1. 解释一下confounding factor
2. 取三点，三个点的correlation是1
（1）有什么办法让玩游戏的人aging up ..
(2) 如果新的月份revenue突然上涨了20%，怎么找原因
(3) 给了一个很简单的表格，三个column，case id，status，和time，问有什么办法只现实最后一个status。codepad上面随便写，但是又没说让写pseudo code还是具体写什么。我用python dataframe写的，然后又问我能不能用R写，我说好多年不用，又让我用sql再写一遍，很神经的操作

像地里其他的朋友说的一样，介绍自己背景。感觉这个 HR 很不专业，对 Roblox 的业务不太熟悉。。。一直在给我念 ppt 一样，说有多少用户，多么 nb 啥啥啥，但是中途念的又老卡壳，不听的额，额，额。然后就像在给我 create profile 一样问 python 几年经验，SQL 几年经验，Hive，Spark，ML，blabla 像个机器人问完后。就是地理说的会问几个 stats 问题，confounding variable是什么，给他举个例子。然后就是pearson correlation 为 1 的三个点，我没听懂啥意思，以为他问我 concept 概念，我说三个点在一条线就是，然后 HR 感觉不太懂，说给她三个点，然后我就给她三个点了，他说 ok。
【HM 电面】
主要就是问 product，case study，如果 Roblox 想在新的country 介绍 Roblox 业务，怎么确定要不要介绍，介绍的话，应该先介绍什么游戏。大概说了一些 metric，说可以在新的国家做一些 survey，然后和类似的现有服务国家做similarity。Roblox 家的 DS 更偏 product analysis，modeling 比较少。

加一个friend interaction feature 怎么evaluate..。我顿时黑线，跟我职位不搭就算了，问问这些其实可以理解， 好在我也准备了，答得还算满意，接下来HM居然跟我聊ads auctions.. 我然后问这个职位需要做ads吗，

第一轮case是有一个外卖公司，某一个metric突然在三四天内下降，like conversion rate，问你有什么想法来解决这个问题。之后会问怎么设计实验来test你的solution，还有各种追问，like怎么分design和control group， 没办法随机分怎么办。. check 1point3acres for more.
第二轮case是如何衡量一个新的游戏matching algorithm？用什么metric，怎么conduct实验，pvalue是啥，power和p-value，如果user group不能随机分成control， experiment怎么办, etc.

SQL题目：
Input
User_id, action, date
Output
Date, received_ct, approved_ct
我的答案
SELECT date count(*) AS ct
FROM
WHERE action = 'received'
GROUP BY
SELECT date, SUM(received_case) AS received_ct, SUM(approvd_Case)/2 AS approved_ct
FROM
(SELECT *, CASE WHEN action = 'received' THEN 1 END AS received_case, CASE WHEN action = 'approved' THEN 2 END AS 'approvd_Case'
FROM table) AS temp.
GROUP BY date


5 coding: 1 SQL ranking, 1 python array indexing，1 python list and sort，1 write t-test on the given dataset （python的都可以用r来做），1 leave one out cross validation 不会做... 求指导
12 选择: 5-6 SQL(join, lag, sum), probability, Bayes' theorem, logistic regression, k-means 找 centroid, regression  beta, one out cross validation
白票oa  也算是查缺补漏了
以下搬运glassdoor
“First round CodeSignal. 17 questions, 2 simple Python data manipulation, SQL queries qs, Python ML implementation, SQL + Math + Probability + ML multiple choices.”

Q1)userid, created_timestamp以及userid, session_start, session_end timestamp求D30 retention rateQ2) how to measure the impact of "recommending friends" on roblox homepage?
make sure to mention the risk. (it replaces a spot on the home page)
.1point3acres
Follow up with AB testing details. . 1point3acres.com
How to calucate sample size
are there social network effect?
what are the metrics?


https://engineering.linkedin.com/blog/2019/06/detecting-interference--an-a-b-test-of-a-b-tests