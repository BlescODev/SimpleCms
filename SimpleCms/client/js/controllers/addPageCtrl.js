app.controller('addPageCtrl', ['appService', '$scope', function (appService, $scope) {

    var init = function () {
        console.log('addPageCtrl got initialized');
    };

    appService.ready(init);

}]);