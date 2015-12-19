var app = angular.module('jsonToHtmlApp', ['ngRoute', 'ngSanitize', 'ngAnimate']);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/add-page', {
            controller: 'addPageCtrl',
            templateUrl: 'html/views/new-page.tpl.html'
        })
        .when('/:content', {
            controller: 'contentCtrl',
            templateUrl: 'html/views/home.tpl.html'
        })
        .when('/:content/:subcontent', {
            controller: 'contentCtrl',
            templateUrl: 'html/views/home.tpl.html'
        })
        .otherwise({
            redirectTo: '/'
        });
}]);

app.service('appService', ['$q', '$location', function($q, $location){

    var properties = [];
    properties["location"] = "http://"+ $location.host() + ":" + $location.port() + "/";

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