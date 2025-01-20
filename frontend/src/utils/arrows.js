import React from "react";

function CustomNextArrow(props) {
	const { className, style, onClick } = props;
	return (
		<div
			className={className}
			style={{ ...style, display: "block", background: "red", right: "5px" }}
			onClick={onClick}
		/>
	);
}

function CustomPrevArrow(props) {
	const { className, style, onClick } = props;
	return (
		<div
			className={className}
			style={{ ...style, display: "block", background: "green", left: "5px" }}
			onClick={onClick}
		/>
	);
}
