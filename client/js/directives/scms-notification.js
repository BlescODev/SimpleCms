app.directive('scmsNotification', function(){
	return {
		restrict: 'E',
		scope: {
			notification: "="
		},
		templateUrl: "/html/directives/scms-notification.tpl.html",
	};
});
