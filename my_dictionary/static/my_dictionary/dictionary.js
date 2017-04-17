$(document).ready(function() {
    $('#find').on('click', function() {
        var url = $('#server-data').attr('data-url')
        var englishWord = $('#english-word').val()
        console.log (englishWord)
        for (chr in englishWord) {
            console.log(englishWord[chr]);
        };
        function insertValue(transcription, russianWord, accessCount) {
          $('#russian-word').val(russianWord);
          $('#transcription').val(transcription);
          $('#access_count').val(accessCount);
        };

        //alert(englishWord.match(/[^a-z]/g).length)
        if (englishWord.match(/[^a-z]/g) != null) {
            msg = 'The word "' + englishWord + '" not exists!';
            alert(msg);
        } else {
            $.ajax({
                url: url + englishWord,
                type: "GET"
            //data:{
            //    'englishWord': englishWord,
           //},
            //dataType: 'text'
           })
            .done(function(data) {
                var obj = $.parseJSON(data);

                if (obj === false) {
                  var msg = 'The word "' + englishWord + '" not is found. To insert it ' +
                           'in the dictionary fill the field ' +
                           '"Russian word" at least!';
                  alert(msg);
                 } else if (obj === englishWord) {
                     insertValue(null, null, null)
                     msg = 'The path "' + englishWord + '" is not a word'
                     alert(msg)
                 } else {
                     insertValue(obj.transcription, obj.russian_word, obj.access_count)
                 }
            });
        }

   });
});
