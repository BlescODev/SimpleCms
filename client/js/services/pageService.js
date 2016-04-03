app.service('pageService', ['appService', '$http', '$q', function(appService, $http, $q){

    var navigationPromise;
    var contentPromise;

    var add = function (page, promise) {
        appService.http("PUT", appService.get("location") + 'pages/', page, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    var get = function (page, promise) {
        appService.http("GET", appService.get("location") + 'pages/' + page, {}, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    var update = function (page, promise) {
        appService.http("POST", appService.get("location") + 'pages/' + page.route, page, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    var remove = function (page, promise) {
        appService.http("DELETE", appService.get("location") + 'pages/' + page.route, {}, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };
    return {
        add: function (page) {
            contentPromise = $q.defer();
            add(page, contentPromise);
            return contentPromise.promise;
        },
        get: function (page) {
            contentPromise = $q.defer();
            get(page, contentPromise);
            return contentPromise.promise;
        },
        update: function (page) {
            contentPromise = $q.defer();
            update(page, contentPromise);
            return contentPromise.promise;
        },
        remove: function (page) {
            contentPromise = $q.defer();
            remove(page, contentPromise);
            return contentPromise.promise;
        }
	
    }
}]);
