"use strict";

const csv2gexf = require('../lib/index');


// -------------------------------------------------------------------------------------------------   


var i=0;
var c = 1932;
while (i<c){
	var config = {
    graphParams: {
        defaultEdgeType: 'undirected',
        meta: {
            description: 'An example graph.',
            creator: 'csv2gexf'
        }
    },
    nodes: {
        file: 'csv/csvout/node'+i+'.csv',
        schema: [
            'id',
            'label',
            
        ],
        parseOptions: {
            columns: true,
            skip_empty_lines: true,
            trim: true
        }
    },
    edges: {
        file: 'csv/csvout/edge'+i+'.csv',
        schema: [
            'source',
            'target'
                   ],
        parseOptions: {
            columns: true,
            skip_empty_lines: true,
            trim: true
        }
    },
    saveAs: 'result/'+i+'.gexf'
};

csv2gexf.convert(config)
    .then(function () {
        console.log("The Gexf file is written.");
    });
i=i+1;    
}
