app = angular.module("twitterApp",[]);

app.controller("twitterAppController",['$scope','$http', function($scope,$http){

$scope.data = {}
$scope.languages = [{'name':'English','value':'en'},
{'name':'Spanish','value':'es'},
{'name':'French','value':'fr'},
{'name':'Portugese','value':'pt'}];

$scope.lang = $scope.languages[0];

$scope.updateLang = function(lang){
   $scope.lang = lang
};

$scope.appID = 'dj0yJmk9NFBiMjFSeTlKbVV0JmQ9WVdrOVNIWTJkVWhUTXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Mw--'

$scope.submitForm = function(){

    if($scope.query != ""){
       $http.post('getResults',data={query:$scope.query,lang:$scope.lang.value}).success(function(d){
            if(d.error){
               alert(d.error)
               $scope.data = d;
               $('#piecontainer').html('')
               return
            }
             
            $scope.data = d;
            var sad = 0;
            var happy = 0
            //var cities = " "
            var cArray = []
            for (var i =0; i < d.result.length; i++)
            {
                if(d.result[i].json.user.location)
                {             
                    cArray.push("'".concat(d.result[i].json.user.location,"'"));
                }
                 
                //else if(d.result[i].json.user.time_zone)
                    //cities=cities.concat("'",d.result[i].json.user.location,"',");
                //console.log(" ".concat(d.result[i].json.user.location).concat(d.result[i].json.user.time_zone));
                if (d.result[i].type == 'happy')
                    happy++
                else
                    sad++
                        //AIzaSyDvzXqCeRfEDo-EUsKGjMRF29KhxYD2I6g
            }
            
            //select * from geo.places.belongtos where placeTypeName.code = 29 and member_woeid  
            
            $scope.pieData = [{
                    type: 'pie',
                    name: 'Sentiment',
                    data: [
                        ['Happy',happy],
                        ['Sad', sad]
                    ]
                }]

        $scope.drawPieChart($scope.pieData);
        //console.log(cities)
        console.log(cArray)
        console.log(cArray.join())
        
//https://query.yahooapis.com/v1/public/yql?q=select%20woeid%2Cname%20%20from%20geo.places%20where%20text%20in%20('Dallas%2C%20TX'%2C'Kolkata'%2C'Worldwide%20-%206k%20team%20followers'%2C'NL'%2C'Roermond'%2C'India%20-Mumbai'%2C'georgia'%2C'Missouri%2C%20USA'%2C'Pawhuska%2C%20Oklah%E2%9D%A4%EF%B8%8Fma'%2C'The%20Woodlands%20-%20TX%20-%20USA'%2C'The%20Woodlands%20-%20TX%20-%20USA'%2C'The%20Woodlands%20-%20TX%20-%20USA'%2C'india'%2C'Delhi'%2C'Mumbai%20-%20Meri%20Jaan'%2C'Chennai'%2C'Pigeon%20Forge%2C%20TN'%2C'Sydney'%2C'WorldWide'%2C'Mumbai'%2C'Los%20Angeles%2C%20CA'%2C'Scotland%2C%20Edinburgh'%2C'tryingto%20%23%5Efi~%7B%7C__%23%7D%25%25*'%2C'Portland%2C%20OR'%2C'Ahmedabad%2FMumbai'%2C'Mankato%2C%20Minnesota'%2C'Canberra%2C%20Australia%20'%2C'India%20'%2C'Kolkata'%2C'USA'%2C'USA'%2C'Guwahati%2C%20India'%2C'Indio%2C%20CA'%2C'Mumbai'%2C'Noida%2C%20India'%2C'Child%20of%20the%20Universe'%2C'Mera%20Bharat%20Mahaan'%2C'Dont%20know%20But%20sure%20in%20India%20'%2C'San%20Jose%20'%2C'70%206a%20St.%20NE%2C%20Calgary%2C%20AB'%2C'Forest%20Lake%2C%20MN%20USA'%2C'Bangalore%2C%20India'%2C'Kansas%20City%2C%20MO'%2C'Pittsburgh'%2C'Enfield%2C%20UK'%2C'Bangalore%2C%20India'%2C'Los%20Angeles%2C%20California%2C%20USA'%2C'delhi'%2C'Forest%20Lake%2C%20MN%20USA'%2C'Killumbus%2C%20OH'%2C'Ahmedabad%2FMumbai'%2C'Swat%20Generation'%2C'Bangalore%2C%20India'%2C'Westeros'%2C'Winnipeg%2C%20Manitoba%2C%20Canada'%2C'Lucknow%20%2C%20India'%2C'South%20Jersey%2FSouth%20Philly'%2C'Worldwide'%2C'Low%20Earth%20Orbit'%2C'Dubai'%2C'Mumbai'%2C'USA'%2C'Mumbai'%2C'India%20'%2C'Murrieta%2C%20CA'%2C'San%20Diego%2CCa.'%2C'UAM-Managua-Esteli-Nicaragua'%2C'Vancouver%2C%20British%20Columbia'%2C'Urbanopolis'%2C'Okinawa%2C%20Japan'%2C'Okinawa%2C%20Japan'%2C'Okinawa%2C%20Japan'%2C'C%C3%B3rdoba'%2C'Urbanopolis'%2C'USA')&format=json&diagnostics=true&callback=        
        
//http://query.yahooapis.com/v1/public/yql?format=json&q=select woeid,name  from geo.places where text in ('Dallas, TX','Kolkata','Worldwide - 6k team followers','NL','Roermond','India -Mumbai','georgia','Missouri, USA','Pawhuska, Oklah❤️ma','The Woodlands - TX - USA','The Woodlands - TX - USA','The Woodlands - TX - USA','india','Delhi','Mumbai - Meri Jaan','Chennai','Pigeon Forge, TN','Sydney','WorldWide','Mumbai','Los Angeles, CA','Scotland, Edinburgh','tryingto #^fi~{|__#}%%*','Portland, OR','Ahmedabad/Mumbai','Mankato, Minnesota','Canberra, Australia ','India ','Kolkata','USA','USA','Guwahati, India','Indio, CA','Mumbai','Noida, India','Child of the Universe','Mera Bharat Mahaan','Dont know But sure in India ','San Jose ','70 6a St. NE, Calgary, AB','Forest Lake, MN USA','Bangalore, India','Kansas City, MO','Pittsburgh','Enfield, UK','Bangalore, India','Los Angeles, California, USA','delhi','Forest Lake, MN USA','Killumbus, OH','Ahmedabad/Mumbai','Swat Generation','Bangalore, India','Westeros','Winnipeg, Manitoba, Canada','Lucknow , India','South Jersey/South Philly','Worldwide','Low Earth Orbit','Dubai','Mumbai','USA','Mumbai','India ','Murrieta, CA','San Diego,Ca.','UAM-Managua-Esteli-Nicaragua','Vancouver, British Columbia','Urbanopolis','Okinawa, Japan','Okinawa, Japan','Okinawa, Japan','Córdoba','Urbanopolis','USA')       
        
        
        
        var baseURL = "https://query.yahooapis.com/v1/public/yql?q="
        var url = baseURL.concat("select woeid,name from geo.places where text in (")
        //url = url.concat(cities.substring(0,cities.length-1) ,')');
        url = url.concat(cArray.join() ,')&format=json&callback=');
        console.log(url)
        $http.get(url).success(function(res){
            if (res.query.count <= 0 )
            {
                alert('Error in retreiving geocodes for tweets')
                return;
            }
            res = res.query.results.place;
            woeids = []
            for(var i =0; i< cArray.length; i++)
            {
                for (var j =0 ; j<res.length; j++)
                    if(cArray[i].toLowerCase().indexOf(res[j].name.toLowerCase()) > -1)
                    {
                        console.log(cArray[i].concat(',',res[j].name,res[j].woeid))
                        woeids.push(res[j].woeid);
                        break;
                    }
            }
            var newurl = baseURL.concat('select * from geo.places.belongtos where placeTypeName.code = 29 and member_woeid in (');
            newurl = newurl.concat(woeids.join(),")&format=json")
            $http.get(newurl).success(function(geoInfo){

                if(geoInfo.query.count <= 0){
                     alert('Error in retreiving geocodes for tweets')
                    return;             
                }
                
                var geoCounts = {'Europe':0,'Asia':0,'NorthAmerica':0,'Africa':0,'SouthAmerica':0,'Antarctic':0,'Australia':0}                
                geoInfo = geoInfo.query.results.place;
                for(var i=0; i<geoInfo.length; i++)
                {
                    switch(geoInfo[i].name){
                        
                        case 'Europe' :
                                    geoCounts.Europe +=1;
                                    break;
                        case 'Asia':
                                    geoCounts.Asia +=1
                                    break;
                        case 'North America':
                                    geoCounts.NorthAmerica +=1
                                    break;
                        case 'Africa':
                                    geoCounts.Africa +=1
                                    break;
                        case 'South America':
                                    geoCounts.SouthAmerica +=1
                                    break;
                        case 'Antarctic':
                                    geoCounts.Antarctic +=1
                                    break;
                        default:
                                    geoCounts.Australia +=1
                                    break;
                                        
                    }                
                }
                
                 $scope.mapData = [{"hc-key": "eu","value": geoCounts.Europe},
                        {"hc-key": "oc","value": geoCounts.Australia},
                        {"hc-key": "af","value": geoCounts.Africa},
                        {"hc-key": "as", "value": geoCounts.Asia},
                        {"hc-key": "na","value": geoCounts.NorthAmerica},
                        {"hc-key": "sa","value": geoCounts.SouthAmerica}];
                // Initiate the chart    
                        $scope.drawMap($scope.mapData);
            }).error(function(){
                alert('could not load geo information for each tweet')
            });
            console.log(woeids);
        }).error(function(er){
            alert('could not load geo information for each tweet')
        });
        
       

        
       }).error(function(error){
            $scope.data={}
            $('#piecontainer').html('')
            alert(error);
       });
    }
}


$scope.drawMap = function(mapData){

    if(!mapData){
        $('#worldcontainer').html(''); 
        return;
    }
    $('#worldcontainer').highcharts('Map', {

        title : {
            text : 'Distribution of tweets'
        },

        subtitle : {
            text : 'Source map: <a href="http://code.highcharts.com/mapdata/custom/world-continents.js">World continents</a>'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0
        },

        series : [{
            data : mapData,
            mapData: Highcharts.maps['custom/world-continents'],
            joinBy: 'hc-key',
            name: '',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }]
    });


}


$scope.drawPieChart = function (pieData){

        if(!pieData){
            $('#piecontainer').html('')
            return 
        }

        $('#piecontainer').highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false
                },
                title: {
                    text: 'Twitter Sentiment Distribution'
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                            style: {
                                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                            }
                        }
                    }
                },
                series:pieData
            });
}

}]);