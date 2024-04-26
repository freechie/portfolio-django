import React, { useState, useEffect, useRef } from "react";
import Slider from "react-slick";
import "flowbite";

class Project {
	constructor({
		id,
		title,
		description,
		contribution_role,
		created_at,
		updated_at,
		status,
		technologies,
		tags,
		images,
		repo_link,
		is_featured,
		link,
	}) {
		this.id = id;
		this.title = title;
		this.description = description;
		this.contributionRole = contribution_role;
		this.createdAt = created_at;
		this.updatedAt = updated_at;
		this.status = status;
		this.technologies = technologies;
		this.tags = tags;
		this.images = images;
		this.repoLink = repo_link;
		this.isFeatured = is_featured;
		this.link = link;
	}
}
export default function ProjectScroller() {
	const [projects, setProjects] = useState(new Map());

	useEffect(() => {
		fetch("http://localhost:8000/api/projects/")
			.then((response) => response.json())
			.then((data) => {
				const newProjects = new Map();
				data.forEach((projectData) => {
					const project = new Project(projectData);
					newProjects.set(project.id, project);
				});
				setProjects(newProjects);
			})
			.catch((error) => console.error("Error fetching projects:", error));
	}, []);

	var settings = {
		initialSlide: 0,
		dots: false,
		lazyLoad: true,
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2500,
		accessibility: true,
		arrows: true,
		pauseOnHover: true,
		speed: 1000,
		fade: true,
		centerMode: true,
		centerPadding: "60px",
		adaptiveHeight: true,
	};

	return (
		<div className="aspect-auto slider-container text-center px-4 dark:bg-neutral-500 bg-neutral-300">
			<Slider {...settings}>
				{Array.from(projects.values()).map((project, index) => (
					<div key={project.id} className="p-4">
						<div className="max-w-fit border rounded-lg shadow dark:bg-gray-800 dark:border-neutral-100 m-4">
							<div className="p-16 m-auto">
								<h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
									{project.title}
								</h5>
							</div>

							<div className="flex justify-center items-center p-4 m-4">
								<a href={`/project/${project.id}/`}>
									<img
										className="rounded-t-lg"
										src={
											project.images.length > 0
												? project.images[0].image
												: "no image"
										}
										alt={project.title}
									/>
								</a>
							</div>
							<div className="flex flex-wrap justify-center gap-2 mb-3">
								<p className="mb-3 font-1xl dark:text-gray-700">
									{project.description}
								</p>
							</div>
							<div className="flex flex-wrap justify-center gap-2 mb-3">
								<p className="text-lg mb-3 text-gray-600 dark:text-gray-400">
									Role: {project.contributionRole}
								</p>
							</div>
							<div className="flex flex-wrap justify-center gap-2 mb-3">
								<p className="bg-blue-200 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 mr-2">
									Tags:{" "}
								</p>
								{project.tags.map((tag) => (
									<span
										key={tag}
										className="bg-blue-200 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800"
									>
										{tag}
									</span>
								))}
							</div>
							<div className="flex flex-wrap justify-center gap-2 my-3">
								<a
									href={project.repoLink || "#"}
									className="inline-flex items-center px-3 py-2 text-md text-center dark:text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
								>
									Github Repo
								</a>
							</div>
						</div>
					</div>
				))}
			</Slider>
		</div>
	);
}
