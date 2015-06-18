/*
[Validating Receipts With the App Store](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateRemotely.html)
[在Corona中如何对apple store的iap订单进行服务器二次验证](http://www.buildapp.net/post/188.htm)
*/
        //解密及base64加密过程

        private string DecodeReceipt(string receipt)
        {
            string postDataStr = "";
            try
            {
                receipt = Regex.Replace(receipt, @"[^0-9a-fA-F]", "");
                string ret = "";
                for (int i = 0; i < receipt.Length; i = i + 2)
                {
                    string tmp = receipt.Substring(i, 2);
                    byte b = byte.Parse(tmp, System.Globalization.NumberStyles.HexNumber);
                    char ch = Convert.ToChar(b);
                    ret += ch;
                }
                byte[] bytes = Encoding.Default.GetBytes(ret);
                postDataStr = "{\"receipt-data\":\"" + Convert.ToBase64String(bytes) + "\"}";
            }
            catch
            {
            }
            return postDataStr;
        }

		
		
		
		//另写一个方法即可
		
        //进行验证

        string postDataStr = DecodeReceipt(Request.Form("receipt"));

        //提交服务器
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://sandbox.itunes.apple.com/verifyReceipt");//https://buy.itunes.apple.com/verifyReceipt
        request.Method = "POST";
        request.ContentType = "application/x-www-form-urlencoded";
        request.ContentLength = postDataStr.Length;
        Stream myRequestStream = request.GetRequestStream();
        StreamWriter myStreamWriter = new StreamWriter(myRequestStream, Encoding.GetEncoding("gb2312"));
        myStreamWriter.Write(postDataStr);
        myStreamWriter.Close();

        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        Stream myResponseStream = response.GetResponseStream();
        StreamReader myStreamReader = new StreamReader(myResponseStream, Encoding.GetEncoding("utf-8"));
        string retString = myStreamReader.ReadToEnd();
        myStreamReader.Close();
        myResponseStream.Close();

        Response.Write(retString);