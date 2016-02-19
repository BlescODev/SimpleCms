var app = angular.module('jsonToHtmlApp', ['ngRoute', 'ngSanitize', 'ngAnimate']);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/add-page', {
            controller: 'addPageCtrl',
            templateUrl: 'views/new-page.tpl.html',
            resolve: function (user) {
                return user.isLoggedIn();
            }
        })
        .when('/login', {
            controller: 'loginCtrl',
            templateUrl: 'views/login.tpl.html'
        })
        .otherwise({
            controller: 'contentCtrl',
            templateUrl: 'views/content.tpl.html'
        });
}]);

app.service('appService', ['$q', '$location', '$http', function($q, $location, $http){

    var properties = [];
    properties["location"] = "http://"+ $location.host() + ":" + $location.port() + "/";
    properties["main"] = "/index";
    properties["blesc"] = "http://blesc.ch:8080";

    var httpRequest = function (url, data, success, error) {

        $http({
            method: "POST",
            url: url,
            headers: {
                'Content-type': 'application/json'
            },
            data: data
        })
            .then(function (response) {
                if(typeof success === 'function'){
                    success(response);
                }
            }, function (response) {
                if(typeof error === 'function'){
                    error(response);
                }
            });

    };
    
    return {
        ready: function (callback) {
            if(typeof callback === 'function'){
                angular.element(document).ready(callback);
            }
        },
        get: function (property) {
            return properties[property];
        },
        http: function (url, data, success, error) {
            httpRequest(url, data, success, error);
        }
    }
}]);
