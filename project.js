
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
          if (this.readyState===4 && this.status === 200){
              callback(this.response);
          }
    }
    request.open("Get", path);
    request.send();
}

function xcode(){
  ajaxGetRequest("/bargraph",bargraph);
  ajaxGetRequest("/linegraph", linegraph);
  //ajaxGetRequest("/scatterplot",scatterplot);

}


function bargraph(response){
  let response = JSON.parse(response);
  let data = [
    {
      x : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      y : response,
      'type': 'bar'
    }
  ];
  let layout = {
  xaxis: {title: 'month'},
  yaxis: {title: '#permits' },
  title: 'Building permits by month, Buffalo NY'
  
};
  plotly.newPlot('bargraph',data,layout);

}
function linegraph(response){
  let response=JSON.parse(response);
  let data=[
    {
      x:[2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
      y:response,
      'type':'line'
    }
  ];
  let layout = {
    xaxis:{title: 'year'},
    yaxis:{title:'# permits'},
    title:'Building permits by year, Buffalo NY'
}
  plotly.newPlot('linegraph',data,layout)
}


