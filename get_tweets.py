import tweepy
import xlsxwriter

ACCESS_TOKEN = "1115463269735653377-FNDF3x6irJ6Pzjc3zj3HzSXqbNKXvA"
ACCESS_TOKEN_SECRET = "0ahplhRefK3Oa7VjuIKqrtEPFc1zC3DFVoExXDk8Stk2A"
CONSUMER_KEY = "XMdcwozYFOlZh66BGVfd1Ukf3"
CONSUMER_SECRET = "cTKsO4vGfyuLtCw3sdqHsbJSGqRpD62b5Rij8yE77F4GHLpqqG"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)



#SearchTerms = "attractive OR bald OR beautiful OR chubby OR clean OR dazzling OR drab OR elegant OR fancy OR fit OR flabby OR glamorous OR gorgeous OR handsome OR long OR magnificent OR muscular OR plain OR plump OR quaint OR scruffy OR shapely OR short OR skinny OR stocky OR ugly OR unkempt OR unsightly OR ashy OR black OR blue OR gray OR green OR icy OR lemon OR mango OR orange OR purple OR red OR salmon OR white OR yellow OR alive OR better OR careful OR clever OR dead OR easy OR famous OR gifted OR hallowed OR helpful OR important OR  inexpensive OR mealy OR mushy OR odd OR poor OR powerful OR rich OR shy OR tender OR  unimportant OR uninterested OR vast OR wrong OR aggressive OR agreeable OR ambitious OR brave OR calm OR delightful OR eager OR faithful OR gentle OR happy OR jolly OR kind OR lively OR nice OR obedient OR polite OR proud OR silly OR thankful OR victorious OR witty OR wonderful OR zealous OR angry OR bewildered OR clumsy OR defeated OR embarrassed OR fierce OR grumpy OR helpless OR itchy OR jealous OR lazy OR mysterious OR nervous OR obnoxious OR panicky OR pitiful OR repulsive OR scary OR thoughtless OR uptight OR worried OR broad OR chubby OR crooked OR curved OR deep OR flat OR high OR hollow OR low OR narrow OR refined OR round OR shallow OR skinny OR square OR steep OR straight OR wide OR big OR colossal OR fat OR gigantic OR great OR huge OR immense OR large OR little OR mammoth OR massive OR microscopic OR miniature OR petite OR puny OR scrawny OR short OR small OR tall OR teeny OR tiny OR crashing OR deafening  OR echoing  OR faint OR harsh OR hissing OR howling OR OR loud OR melodic OR noisy OR purring OR quiet OR rapping OR raspy OR rhythmic OR screeching OR shrilling OR squeaking OR thundering OR tinkling OR wailing OR whining OR whispering OR ancient OR brief OR early OR fast OR future OR late OR long OR modern OR old OR old-fashioned OR prehistoric OR quick OR rapid OR short OR slow OR swift OR young OR acidic OR bitter OR cool OR creamy OR delicious OR disgusting OR fresh OR greasy OR juicy OR hot OR moldy OR nutritious OR nutty OR putrid OR rancid OR ripe OR rotten OR salty OR savory OR sour OR spicy OR spoiled OR stale OR sweet OR tangy OR tart OR tasteless OR tasty OR yummy OR breezy OR bumpy OR chilly OR cold OR cool OR cuddly OR damaged OR damp OR dirty OR dry OR flaky OR fluffy OR freezing OR greasy OR hot OR icy OR loose OR melted OR prickly OR rough OR shaggy OR sharp OR slimy OR sticky OR strong OR tight OR uneven OR warm OR weak OR wet OR wooden OR abundant OR billions OR enough OR few OR full OR hundreds OR incalculable OR limited OR little OR many OR most OR millions OR numerous OR scarce OR some OR sparse OR substantial OR thousands OR gud OR badd OR rel OR rell OR really OR dutty OR niceness OR tight OR fancy OR hoss OR fuckery OR shit OR sickening OR dope OR personally OR don't OR at OR me OR I OR cool OR nice OR amazing OR fun OR scenes OR wayy OR wayyy OR wayyyy freezing OR greasy OR hot OR icy OR loose OR melted OR prickly OR rough OR shaggy OR sharp OR slimy OR sticky OR strong OR tight OR uneven OR warm OR weak OR wet OR wooden OR abundant OR billions OR enough OR few OR full OR hundreds OR incalculable OR limited OR little OR many OR most OR millions OR numerous OR scarce OR some OR sparse OR substantial OR thousands OR gud OR badd OR rel OR rell OR really OR dutty OR niceness OR tight OR fancy OR hoss OR fuckery OR shit OR sickening OR dope OR personally OR don't OR at OR me OR I OR cool OR nice OR amazing OR fun OR scenes OR wayy OR wayyy OR wayyyy"



print("Fetching tweets...")

text_file = open("tweets.txt", "w", encoding="utf-8")
#workbook = xlsxwriter.Workbook("tweets.xlsx")
#worksheet = workbook.add_worksheet()

places = api.geo_search(query="Trinidad and Tobago", granularity="country")
place_id = places[0].id

row = 0
col = 0
for tweet in tweepy.Cursor(api.search, lang="en", geocode="10.4576,-61.2414,90km", q="place:%s " % place_id, tweet_mode="extended").items(1000):
    #worksheet.write(row,col, str(tweet.full_text))
    #row += 1
    text_file.write(tweet.full_text + "\n")
text_file.close()
#workbook.close()

print("Done!\n", "Saved in tweets.txt")
