const csv = require('csv-parser');
const fs = require('fs');
const performance = require('perf_hooks').performance;
var results = [];
var tour;

/**
 * This funtion return a fully of 0's matrix
 *
 * @param {*} m width of matrix
 * @param {*} n height of matrix
 * @returns a matrix of m x n full of 0's
 */
function matrix(m, n) {
    var result = [];
    for (var i = 0; i < n; i++) {
        result.push(new Array(m).fill(0));
    }
    return result;
}


var timeStart = performance.now();

fs.createReadStream('outfile.csv')
    .pipe(csv())
    .on('data', (data) => {
        results.push(data);
    })
    .on('end', () => {
        console.log(results[0]);
        console.log(results.length);
        tour = matrix(results.length, results.length);
        var cityNumbers = results.length;
        for (var i = 0; i < results.length; i++) {
            for (var j = 0; j < results.length; j++) {
                // This multiples per 100 to get a more realistic result
                tour[i][j] = (Math.abs(results[i]['COORD_X'] - results[j]['COORD_X']) + Math.abs(results[i]['COORD_Y'] - results[j]['COORD_Y'])) * 100;
            }
        }
        var path = new Array(cityNumbers);
        var bestpath = new Array(cityNumbers);
        var cost = 0;
        var bestcost = Number.MAX_SAFE_INTEGER;

        /**
         * This function solve the TSP with a backtracking strategy
         *
         * @param {*} t the current position 
         */
        function tsp_backtrack(t) {
            var i, j;
            if (t == cityNumbers - 1) {
                if (tour[path[t - 1]][path[t]] != 0 && tour[path[t]][0] != 0) {
                    if (cost + tour[path[t]][0] < bestcost && tour[path[t]][0] != 0) {
                        bestcost = cost + tour[path[t]][0];
                        for (j = 0; j <= cityNumbers - 1; j++)
                            bestpath[j] = path[j];
                    }
                }
            } else {
                for (j = t - 1; j <= cityNumbers - 1; j++) {
                    console.log(path);
                    if (tour[path[t - 1]][path[j]] != 0 && cost + tour[path[t - 1]][path[j]] < bestcost) {
                        var temp;
                        temp = path[t];
                        path[t] = path[j];
                        path[j] = temp;
                        cost += tour[path[t - 1]][path[t]];
                        tsp_backtrack(t + 1);
                        cost -= tour[path[t - 1]][path[t]];
                        temp = path[t];
                        path[t] = path[j];
                        path[j] = temp;
                    }
                }
            }
        }
        console.log('Matrix shows below: ');
        console.log(tour);
        for (var i = 0; i <= cityNumbers - 1; i++) {
            path[i] = i;
        }

        console.log('Suppose the traveler begins at Point A, the first point.');
        tsp_backtrack(1);

        for (var i = 0; i <= cityNumbers - 1; i++) {
            console.log(results[bestpath[i]]['NOMBRE']);
            console.log('->');
        }

        var length = 0;
        for (var i = 0; i <= cityNumbers - 2; i++)
            length += tour[bestpath[i]][bestpath[i + 1]];
        length += tour[bestpath[cityNumbers - 1]][0];
        console.log(length);
        var timeEnd = performance.now();
        console.log("The problem for "+ results.length + " cities took "+ (timeEnd - timeStart) + " milliseconds");
    });


