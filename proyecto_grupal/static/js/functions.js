    $(document).ready(function(){
        $('#toggle-btn').click(function(){
            $('#toggle1').attr('style', '');
            $('#toggle2').attr('style', 'visibility: hidden;')
        })
        $('#toggle-btn2').click(function(){
            $('#toggle1').attr('style', 'visibility: hidden;');
            $('#toggle2').attr('style', '')
        })

    })
