    $(document).ready(function(){
        $('#toggle-btn').click(function(){
            $('#toggle1').attr('style', '');
            $('#toggle-btn').addClass('btn-selected')
            $('#toggle2').attr('style', 'visibility: hidden;')
            $('#toggle-btn2').removeClass('btn-selected')

        })
        $('#toggle-btn2').click(function(){
            $('#toggle1').attr('style', 'visibility: hidden;');
            $('#toggle-btn').removeClass('btn-selected')
            $('#toggle2').attr('style', '')
            $('#toggle-btn2').addClass('btn-selected')
        })

    })
