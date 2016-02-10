var app = angular.module('jsonToHtmlApp', ['ngRoute', 'ngSanitize', 'ngAnimate']);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/add-page', {
            controller: 'addPageCtrl',
            templateUrl: 'html/views/new-page.tpl.html'
        })
        .otherwise({
            controller: 'contentCtrl',
            templateUrl: 'html/views/content.tpl.html'
        });
}]);

app.service('appService', ['$q', '$location', function($q, $location){

    var properties = []
    properties["location"] = "http://"+ $location.host() + ":" + $location.port() + "/"
    properties["main"] = "/index"
    
    return {
        ready: function (callback) {
            if(typeof callback === 'function'){
                angular.element(document).ready(callback);
            }
        },
        get: function (property) {
            return properties[property];
        }
    }
}]);
