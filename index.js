var cityNumbers = 6;
var jour = [[0,	3,	1,	5,	8, 3], 
            [3,	0,	6,	7,	9, 6], 
            [1,	6,	0,	4,	2, 7], 
            [5,	7,	4,	0,	3, 4], 
            [8,	9,	2,	3,	0, 1],
            [8,	9,	2,	3,	0, 1]];

var path = new Array(cityNumbers);
var bestpath = new Array(cityNumbers);
var cost = 0;
var bestcost = Number.MAX_SAFE_INTEGER;

function swap(a,b){
    var temp;
    temp = a;
    a = b;
    b = temp;
}


function tsp_backtrack(t){
    var i,j;
    if ( t == cityNumbers -1) {
        if(jour[path[t-1]][path[t]]!=0&&jour[path[t]][0]!=0){
            if(cost+jour[path[t]][0]<bestcost&&jour[path[t]][0]!=0) {
				bestcost=cost+jour[path[t]][0];
				for(j=0; j<=cityNumbers-1; j++)  
                    bestpath[j]=path[j];
            }
        }	
    } else {
        for(j=t-1;j<=cityNumbers-1;j++) {
			if(jour[path[t-1]][path[j]]!=0 && cost+jour[path[t-1]][path[j]]<bestcost)
			{
                var temp;
                temp = path[t];
                path[t] = path[j];
                path[j] = temp;
                cost+=jour[path[t-1]][path[t]];
				tsp_backtrack(t+1);
                cost-=jour[path[t-1]][path[t]];
                temp = path[t];
                path[t] = path[j];
                path[j] = temp;
			}
		}
    }								
}
console.log('Matrix shows below: ');
console.log(jour);
for(var i=0;i<=cityNumbers-1;i++)
{
    path[i]=i;
}

console.log('Suppose the traveler begins at Point A, the first point.');
tsp_backtrack(1);

for(var i=0;i<=cityNumbers-1;i++){
    console.log(bestpath[i]);
    console.log('->');
}

var length=0;
for(var i=0;i<=cityNumbers-2;i++)
    length+=jour[bestpath[i]][bestpath[i+1]];
length+=jour[bestpath[cityNumbers-1]][0];

console.log(length);

