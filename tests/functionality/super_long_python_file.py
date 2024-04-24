import pandas as pd
from datetime import datetime

dora_data = [
	{
		"componentsperday": 332,
		"meantimetoresolve": 0,
		"leadtimetochange": 9.921686746987952,
		"Date": 1691433000000
	},
	{
		"componentsperday": 156,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.8333333333333337,
		"Date": 1691519400000
	},
	{
		"componentsperday": 179,
		"meantimetoresolve": 0,
		"leadtimetochange": 7.033519553072626,
		"Date": 1691605800000
	},
	{
		"componentsperday": 135,
		"meantimetoresolve": 3,
		"leadtimetochange": 4.733333333333333,
		"Date": 1691692200000
	},
	{
		"componentsperday": 69,
		"meantimetoresolve": 0,
		"leadtimetochange": 1.1014492753623189,
		"Date": 1691778600000
	},
	{
		"componentsperday": 17,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.0588235294117647,
		"Date": 1691865000000
	},
	{
		"componentsperday": 304,
		"meantimetoresolve": 443,
		"leadtimetochange": 4.434210526315789,
		"Date": 1691951400000
	},
	{
		"componentsperday": 208,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.264423076923077,
		"Date": 1692037800000
	},
	{
		"componentsperday": 271,
		"meantimetoresolve": 0,
		"leadtimetochange": 5.409594095940959,
		"Date": 1692124200000
	},
	{
		"componentsperday": 431,
		"meantimetoresolve": 0,
		"leadtimetochange": 17.08584686774942,
		"Date": 1692210600000
	},
	{
		"componentsperday": 433,
		"meantimetoresolve": 0,
		"leadtimetochange": 9.030023094688222,
		"Date": 1692297000000
	},
	{
		"componentsperday": 162,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.4506172839506173,
		"Date": 1692383400000
	},
	{
		"componentsperday": 7,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1692469800000
	},
	{
		"componentsperday": 365,
		"meantimetoresolve": 1055,
		"leadtimetochange": 4.780821917808219,
		"Date": 1692556200000
	},
	{
		"componentsperday": 353,
		"meantimetoresolve": 216,
		"leadtimetochange": 4.9405099150141649,
		"Date": 1692642600000
	},
	{
		"componentsperday": 336,
		"meantimetoresolve": 0,
		"leadtimetochange": 5.4523809523809529,
		"Date": 1692729000000
	},
	{
		"componentsperday": 157,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.515923566878981,
		"Date": 1692815400000
	},
	{
		"componentsperday": 227,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.788546255506608,
		"Date": 1692901800000
	},
	{
		"componentsperday": 40,
		"meantimetoresolve": 0,
		"leadtimetochange": 15.925,
		"Date": 1692988200000
	},
	{
		"componentsperday": 21,
		"meantimetoresolve": 0,
		"leadtimetochange": 1.8095238095238096,
		"Date": 1693074600000
	},
	{
		"componentsperday": 134,
		"meantimetoresolve": 0,
		"leadtimetochange": 6.41044776119403,
		"Date": 1693161000000
	},
	{
		"componentsperday": 265,
		"meantimetoresolve": 0,
		"leadtimetochange": 13.818867924528302,
		"Date": 1693247400000
	},
	{
		"componentsperday": 158,
		"meantimetoresolve": 0,
		"leadtimetochange": 4.987341772151899,
		"Date": 1693333800000
	},
	{
		"componentsperday": 451,
		"meantimetoresolve": 0,
		"leadtimetochange": 9.279379157427938,
		"Date": 1693420200000
	},
	{
		"componentsperday": 331,
		"meantimetoresolve": 24,
		"leadtimetochange": 7.637462235649547,
		"Date": 1693506600000
	},
	{
		"componentsperday": 144,
		"meantimetoresolve": 473,
		"leadtimetochange": 4.826388888888889,
		"Date": 1693593000000
	},
	{
		"componentsperday": 4,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.5,
		"Date": 1693679400000
	},
	{
		"componentsperday": 344,
		"meantimetoresolve": 744,
		"leadtimetochange": 5.77906976744186,
		"Date": 1693765800000
	},
	{
		"componentsperday": 367,
		"meantimetoresolve": 23,
		"leadtimetochange": 5.615803814713897,
		"Date": 1693852200000
	},
	{
		"componentsperday": 281,
		"meantimetoresolve": 0,
		"leadtimetochange": 18.416370106761567,
		"Date": 1693938600000
	},
	{
		"componentsperday": 457,
		"meantimetoresolve": 0,
		"leadtimetochange": 23.792122538293218,
		"Date": 1694025000000
	},
	{
		"componentsperday": 240,
		"meantimetoresolve": 0,
		"leadtimetochange": 1.825,
		"Date": 1694111400000
	},
	{
		"componentsperday": 57,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.45614035087719298,
		"Date": 1694197800000
	},
	{
		"componentsperday": 60,
		"meantimetoresolve": 0,
		"leadtimetochange": 27.25,
		"Date": 1694284200000
	},
	{
		"componentsperday": 389,
		"meantimetoresolve": 0,
		"leadtimetochange": 4.29305912596401,
		"Date": 1694370600000
	},
	{
		"componentsperday": 206,
		"meantimetoresolve": 7,
		"leadtimetochange": 6.349514563106796,
		"Date": 1694457000000
	},
	{
		"componentsperday": 180,
		"meantimetoresolve": 0,
		"leadtimetochange": 5.572222222222222,
		"Date": 1694543400000
	},
	{
		"componentsperday": 189,
		"meantimetoresolve": 38,
		"leadtimetochange": 2.4761904761904764,
		"Date": 1694629800000
	},
	{
		"componentsperday": 366,
		"meantimetoresolve": 8,
		"leadtimetochange": 9.295081967213115,
		"Date": 1694716200000
	},
	{
		"componentsperday": 25,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.76,
		"Date": 1694802600000
	},
	{
		"componentsperday": 0,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1694889000000
	},
	{
		"componentsperday": 148,
		"meantimetoresolve": 0,
		"leadtimetochange": 6.952702702702703,
		"Date": 1694975400000
	},
	{
		"componentsperday": 163,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.950920245398773,
		"Date": 1695061800000
	},
	{
		"componentsperday": 112,
		"meantimetoresolve": 0,
		"leadtimetochange": 18.535714285714286,
		"Date": 1695148200000
	},
	{
		"componentsperday": 146,
		"meantimetoresolve": 0,
		"leadtimetochange": 5.773972602739726,
		"Date": 1695234600000
	},
	{
		"componentsperday": 613,
		"meantimetoresolve": 12,
		"leadtimetochange": 136.42088091353998,
		"Date": 1695321000000
	},
	{
		"componentsperday": 108,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.2685185185185188,
		"Date": 1695407400000
	},
	{
		"componentsperday": 1,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1695493800000
	},
	{
		"componentsperday": 271,
		"meantimetoresolve": 46,
		"leadtimetochange": 25.44649446494465,
		"Date": 1695580200000
	},
	{
		"componentsperday": 369,
		"meantimetoresolve": 0,
		"leadtimetochange": 16.471544715447157,
		"Date": 1695666600000
	},
	{
		"componentsperday": 287,
		"meantimetoresolve": 63,
		"leadtimetochange": 9.508710801393729,
		"Date": 1695753000000
	},
	{
		"componentsperday": 359,
		"meantimetoresolve": 7,
		"leadtimetochange": 6.933147632311978,
		"Date": 1695839400000
	},
	{
		"componentsperday": 234,
		"meantimetoresolve": 0,
		"leadtimetochange": 16.482905982905984,
		"Date": 1695925800000
	},
	{
		"componentsperday": 29,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.13793103448275863,
		"Date": 1696012200000
	},
	{
		"componentsperday": 34,
		"meantimetoresolve": 0,
		"leadtimetochange": 24.235294117647059,
		"Date": 1696098600000
	},
	{
		"componentsperday": 74,
		"meantimetoresolve": 396,
		"leadtimetochange": 11.324324324324325,
		"Date": 1696185000000
	},
	{
		"componentsperday": 300,
		"meantimetoresolve": 0,
		"leadtimetochange": 4.386666666666667,
		"Date": 1696271400000
	},
	{
		"componentsperday": 359,
		"meantimetoresolve": 0,
		"leadtimetochange": 12,
		"Date": 1696357800000
	},
	{
		"componentsperday": 85,
		"meantimetoresolve": 0,
		"leadtimetochange": 7.91764705882353,
		"Date": 1696444200000
	},
	{
		"componentsperday": 64,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.453125,
		"Date": 1696530600000
	},
	{
		"componentsperday": 46,
		"meantimetoresolve": 0,
		"leadtimetochange": 4.456521739130435,
		"Date": 1696617000000
	},
	{
		"componentsperday": 9,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.2222222222222222,
		"Date": 1696703400000
	},
	{
		"componentsperday": 129,
		"meantimetoresolve": 0,
		"leadtimetochange": 23.651162790697677,
		"Date": 1696789800000
	},
	{
		"componentsperday": 122,
		"meantimetoresolve": 0,
		"leadtimetochange": 5.60655737704918,
		"Date": 1696876200000
	},
	{
		"componentsperday": 56,
		"meantimetoresolve": 0,
		"leadtimetochange": 6.392857142857143,
		"Date": 1696962600000
	},
	{
		"componentsperday": 82,
		"meantimetoresolve": 0,
		"leadtimetochange": 4.951219512195122,
		"Date": 1697049000000
	},
	{
		"componentsperday": 60,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.716666666666667,
		"Date": 1697135400000
	},
	{
		"componentsperday": 23,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.6086956521739131,
		"Date": 1697221800000
	},
	{
		"componentsperday": 4,
		"meantimetoresolve": 0,
		"leadtimetochange": 2,
		"Date": 1697308200000
	},
	{
		"componentsperday": 79,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.8734177215189877,
		"Date": 1697394600000
	},
	{
		"componentsperday": 148,
		"meantimetoresolve": 0,
		"leadtimetochange": 12.891891891891892,
		"Date": 1697481000000
	},
	{
		"componentsperday": 119,
		"meantimetoresolve": 0,
		"leadtimetochange": 11.663865546218487,
		"Date": 1697567400000
	},
	{
		"componentsperday": 225,
		"meantimetoresolve": 0,
		"leadtimetochange": 25.56,
		"Date": 1697653800000
	},
	{
		"componentsperday": 84,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.2261904761904764,
		"Date": 1697740200000
	},
	{
		"componentsperday": 61,
		"meantimetoresolve": 0,
		"leadtimetochange": 0.21311475409836065,
		"Date": 1697826600000
	},
	{
		"componentsperday": 59,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.0338983050847458,
		"Date": 1697913000000
	},
	{
		"componentsperday": 198,
		"meantimetoresolve": 0,
		"leadtimetochange": 16.525252525252527,
		"Date": 1697999400000
	},
	{
		"componentsperday": 136,
		"meantimetoresolve": 0,
		"leadtimetochange": 2.2205882352941179,
		"Date": 1698085800000
	},
	{
		"componentsperday": 112,
		"meantimetoresolve": 0,
		"leadtimetochange": 28.8125,
		"Date": 1698172200000
	},
	{
		"componentsperday": 111,
		"meantimetoresolve": 0,
		"leadtimetochange": 18.117117117117119,
		"Date": 1698258600000
	},
	{
		"componentsperday": 147,
		"meantimetoresolve": 0,
		"leadtimetochange": 3.061224489795918,
		"Date": 1698345000000
	},
	{
		"componentsperday": 1,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1698431400000
	},
	{
		"componentsperday": 0,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1698517800000
	},
	{
		"componentsperday": 54,
		"meantimetoresolve": 0,
		"leadtimetochange": 17.203703703703704,
		"Date": 1698604200000
	},
	{
		"componentsperday": 89,
		"meantimetoresolve": 0,
		"leadtimetochange": 11.146067415730338,
		"Date": 1698690600000
	},
	{
		"componentsperday": 104,
		"meantimetoresolve": 0,
		"leadtimetochange": 53.875,
		"Date": 1698777000000
	},
	{
		"componentsperday": 163,
		"meantimetoresolve": 0,
		"leadtimetochange": 32.94478527607362,
		"Date": 1698863400000
	},
	{
		"componentsperday": 212,
		"meantimetoresolve": 0,
		"leadtimetochange": 55.424528301886798,
		"Date": 1698949800000
	},
	{
		"componentsperday": 0,
		"meantimetoresolve": 0,
		"leadtimetochange": 0,
		"Date": 1699036200000
	},
	{
		"componentsperday": 4,
		"meantimetoresolve": 0,
		"leadtimetochange": 85.5,
		"Date": 1699122600000
	},
	{
		"componentsperday": 87,
		"meantimetoresolve": 0,
		"leadtimetochange": 26.344827586206898,
		"Date": 1699209000000
	},
	{
		"componentsperday": 40,
		"meantimetoresolve": 0,
		"leadtimetochange": 9.5,
		"Date": 1699295400000
	},
	{
		"componentsperday": 15,
		"meantimetoresolve": 0,
		"leadtimetochange": 1.9333333333333334,
		"Date": 1699381800000
	}
]

def metrics_analysis_html(data):
	''' Function to provide metrics analysis in html '''
	for entry in data:
		entry['Date'] = datetime.utcfromtimestamp(entry['Date'] / 1000.0).strftime('%Y-%m-%d') # Convert timestamp to datetime

	df = pd.DataFrame(dora_data) # Convert data to a Pandas DataFrame
	descriptive_stats = df.describe() # Data summary
	summary_in_html = descriptive_stats.to_html() # Present results in HTML
	return summary_in_html

metrics_analysis_html(dora_data)

