function papagotrans(str_data, source_lang, target_lang) {
  var request_url = "https://openapi.naver.com/v1/papago/n2mt";
  var client_id = "";
  var client_secret = "";
  var text = encodeURIComponent(str_data);
  var payload_data =
    "source=" + source_lang + "&target=" + target_lang + "&text=" + text;
  var options = {
    method: "post",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Naver-Client-Id": client_id,
      "X-Naver-Client-Secret": client_secret,
    },
    payload: payload_data,
  };
  var request = UrlFetchApp.fetch(request_url, options);
  var ret_temp = JSON.parse(request.getContentText()).message.result
    .translatedText;
  return ret_temp;
}
