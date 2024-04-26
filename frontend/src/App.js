import React from "react";
import ProjectScroller from "./components/ProjectScroller";
import UserProfile from "./components/UserProfile";
import RecentProjectsHeader from "./components/RecentProjectsHeader";

const App = () => {
	return (
		<main className="min-h-screen flex flex-col lg:flex-row overflow-hidden">
			{" "}
			{/* Use column layout on small screens and row layout on large screens */}
			{/* Main Content Column */}
			<div className="flex-grow flex flex-col items-center overflow-visible lg:order-2">
				{" "}
				{/* Change order on large screens */}
				<header className="flex-grow w-fit overflow-visible m-auto ">
					<RecentProjectsHeader />
				</header>
				<div className="flex-grow w-full max-w-xl overflow-scroll">
					<ProjectScroller />
				</div>
			</div>
			{/* Side Column for UserProfile, initially on top on small screens */}
			<div className="flex flex-grow justify-center w-fit lg:w-1/5 items-center px-6 py-6">
				{" "}
				{/* Full width on small screens, sidebar width on large screens */}
				<UserProfile />
			</div>
		</main>
	);
};

export default App;
