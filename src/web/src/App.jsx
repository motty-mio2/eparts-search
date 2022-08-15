import React from "react";
import axios from "axios";

function App() {
	const [data, setData] = React.useState();
	const text = React.useRef(null);
	var t;
	const url = "http://127.0.0.1:4000";


	const GetData = () => {
		console.log(text.current.value);
		axios.get(url + "/test/", { params: { query: text.current.value } }).then((res) => {
			setData(res.data);
		});
	};

	return (
		<div>
			<input ref={text} type="text" />
			<div>ここに処理を書いていきます</div>
			<button onClick={GetData}>データを取得</button>
			<div>{data}</div>
		</div>
	);
}

export default App;


