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

    var update = function (contentName, promise) {
        appService.http("POST", appService.get("location") + 'pages/' + page.route, page, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    var remove = function (contentName, promise) {
        appService.http("DELETE", appService.get("location") + 'pages/' + page.route, {}, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };
    return {
        add: function (page) {
            contentPromise = $q.defer();
            add(contentName, contentPromise);
            return contentPromise.promise;
        },
        get: function (contentName) {
            contentPromise = $q.defer();
            get(contentName, contentPromise);
            return contentPromise.promise;
        },
        update: function (contentName) {
            contentPromise = $q.defer();
            update(contentName, contentPromise);
            return contentPromise.promise;
        },
        remove: function (contentName) {
            contentPromise = $q.defer();
            remove(contentName, contentPromise);
            return contentPromise.promise;
        }
	
    }
}]);
