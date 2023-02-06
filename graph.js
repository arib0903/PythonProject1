function getData(){
  let data = ajaxGetRequest("graphBar", plotBar)
  let data2 = ajaxGetRequest("graphPie", plotPie)
  return data
//   return data2
}

function plotBar(data){
    let data_updated = JSON.parse(data)
    console.log(data_updated)
    let lis1 = []
    let lis2 = []
    for(let find of Object.keys(data_updated)){
        let x = find;
        let y = data_updated[find];
        lis1.push(x)
        lis2.push(y)
        
        let data = [{"x": lis1,"y": lis2, type: 'bar'}];
        let layout = {
    "title": "Fully Vaccinated By Location",
    "xaxis":{"title":'Locations'},
    "yaxis":{'title':'% Fully Vaccinated'}
    };
    Plotly.newPlot('barChart', data,layout);
    }
   
}




function plotPie(data2){
    let data_updated = JSON.parse(data2)
    console.log(data_updated)
    let lis1 = []
    let lis2 = []
    for(let find of Object.keys(data_updated)){
        let values = data_updated[find];
        let labels = find;
        lis1.push(values)
        lis2.push(labels)
        
        let data2 = [{"values": lis1,"labels": lis2, type: 'pie'}];
         let layout = {
         height: 400,
         width: 500,
         "title": "Vaccine Manufacturer Market Share"
    };

    Plotly.newPlot('pieChart', data2, layout);
    }

}


// let s = document.getElementById('locText').value;

function getLocData(){
  let user_input_value = document.getElementById('locText').value;
  // console.log(user_input_value)
  let d= {'location':user_input_value}
  let dJson = JSON.stringify(d)
  // console.log(dJson)
  ajaxPostRequest("graphLine", dJson, plotLine)
  // ajaxGetRequest("graphLine", plotLine)
}


function plotLine(data3){
    let data_updated = JSON.parse(data3)
    let user_input_value = document.getElementById('locText').value
      // console.log(data_updated)
    let lis1 = []
    let lis2 = []
    for(let find of Object.keys(data_updated)){
        let x = find;
        let y = data_updated[find];
        lis1.push(x)
        lis2.push(y)
        
        let data3 = [{"x": lis1,"y": lis2}];
        let layout = {
    "title": "% of " + user_input_value + " Fully Vaccinated",
    "xaxis":{"title":'Date'},
    "yaxis":{'title':'% Fully Vaccinated'}
    };
  Plotly.newPlot('lineGraph', data3,layout);
  }
  
}

