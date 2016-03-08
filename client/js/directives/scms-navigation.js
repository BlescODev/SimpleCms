app.directive('scmsNavigation', function($compile){
	return {
		restrict: 'E',
		scope: {
			navigation: "="
		},
		templateUrl: "/html/directives/scms-navigation.tpl.html",
		compile: function(tElement, tAttr) {
			var contents = tElement.contents().remove();
			var compiledContents;

			return function(scope, iElement, iAttr) {
				if(!compiledContents) {
					compiledContents = $compile(contents);
				}
				compiledContents(scope, function(clone, scope) {
					iElement.append(clone); 
				});
			};
		}
	};
});
