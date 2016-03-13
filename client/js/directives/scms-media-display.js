app.directive('scmsMediaDisplay', function(){
	return {
		restrict: 'E',
		scope: {
			media: "="
		},
		templateUrl: "/html/directives/scms-media-display.tpl.html"
	};
});
