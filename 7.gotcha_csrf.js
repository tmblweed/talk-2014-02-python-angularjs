.config(function ($httpProvider) {
  var csrfToken = getCsrfToken();  // Implementation-dependent
  $httpProvider.defaults.headers.common['X-CSRFToken'] = csrfToken;
})
