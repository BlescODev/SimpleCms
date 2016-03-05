app.controller('editPageCtrl', ['appService', 'pageService', '$scope', function(appService, pageService, $scope){

    var init = function () {
        url = getUrl();
        if(url === '') {
            url = appService.get('main');
        }

        url = url.substr(1)

	pageService.get(url).then(function (response) {
            $scope.page = response.data;
        }, function (response) {
            if (response.status == 500) {
                appService.notifications.queue({
                    message: "The server is experiencing some problems at the moment. Sorry!",
                    type: "error"
                });
            }
        });

    };

    $scope.save = function () {
	page = {
            "page": $scope.page
        }

        if(page.id === ''){
            pageService.add(page).then(function (response) {
                $scope.page = response.data;
                appService.$location.url('#/'+ getUrl());
            }, function (response) {
                if (response.status == 500) {
                    appService.notifications.queue({
                        message: "The server is experiencing some problems at the moment. Sorry!",
                        type: "error"
                    });
                }
            });
        } else {
            pageService.update(page).then(function (response) {
                $scope.page = response.data;
	        appService.$location.url('#/'+ getUrl());
            }, function (response) {
                if (response.status == 500) {
                    appService.notifications.queue({
                        message: "The server is experiencing some problems at the moment. Sorry!",
                        type: "error"
                    });
                }
            });
        }
    };

    var getUrl = function() {
        var url = appService.$location.url();

        url = url.substr(5);
        if (!url) {
            return ''
        }
        return url.substr(1);
    };
    appService.ready(init);
}]);
