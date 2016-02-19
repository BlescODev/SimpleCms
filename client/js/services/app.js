var app = angular.module('jsonToHtmlApp', ['ngRoute', 'ngSanitize', 'ngAnimate', 'satellizer']);

app.config(['$routeProvider', '$authProvider', function ($routeProvider, $authProvider) {

    $authProvider.loginUrl = "/auth";
    $authProvider.tokenName = "access_token";

    $routeProvider
        .when('/add-page', {
            controller: 'addPageCtrl',
            templateUrl: 'html/views/new-page.tpl.html',
            resolve: {
                auth: function ($q, $location, user) {

                    var loggedIn = $q.defer();

                    if(user.isLoggedIn()){
                        loggedIn.resolve();
                    } else {
                        loggedIn.reject();
                        $location.url("/login");
                    }

                    return loggedIn.promise;
                }
            }
        })
        .when('/login', {
            controller: 'loginCtrl',
            templateUrl: 'html/views/login.tpl.html'
        })
        .otherwise({
            controller: 'contentCtrl',
            templateUrl: 'html/views/content.tpl.html'
        });
}]);

app.service('appService', ['$q', '$location', '$http', function($q, $location, $http){

    var properties = [];
    properties["location"] = "http://"+ $location.host() + ":" + $location.port() + "/";
    properties["main"] = "/index";

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
        },
        $location: $location
    }
}]);
