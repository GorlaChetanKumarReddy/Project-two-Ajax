function usernameValidation()
{
    var username = document.getElementById("usern").value;
    var param = "userna="+username;
    var requestt = new XMLHttpRequest();
    requestt.onreadystatechange = CheckUserName;
    requestt.open("POST", "http://127.0.0.1:8000/Check_User_Name_Ajax/", true);
    requestt.getResponseHeader('Content-Type', 'application/x-www-form-urlencoded');
    requestt.send(param);

    function CheckUserName()
    {
        if (requestt.readyState == 4)
        {
            var json_data = JSON.parse(requestt.responseText);
            spanelemen = document.getElementById('usspan');
            if (json_data.error == 'username is exists')
            {
                spanelemen.style.color = "red"
                spanelemen.innerText = "username is exists"
                document.getElementById('bt1').disabled = true
            }
            else
            {
                spanelemen.style.color = "green"
                spanelemen.innerText = json_data.message;
                document.getElementById('bt1').disabled = false

            }
        }
    }

}

