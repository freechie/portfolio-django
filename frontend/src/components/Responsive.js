import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// Definition of the Project class to encapsulate project data
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

	// Custom arrow components for the slider
	function CustomNextArrow(props) {
		const { className, style, onClick } = props;
		return (
			<div
				className={className}
				style={{ ...style, display: "block", right: "5px" }}
				onClick={onClick}
			/>
		);
	}

	function CustomPrevArrow(props) {
		const { className, style, onClick } = props;
		return (
			<div
				className={className}
				style={{ ...style, display: "block", left: "5px" }}
				onClick={onClick}
			/>
		);
	}

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
		nextArrow: <CustomNextArrow />,
		prevArrow: <CustomPrevArrow />,
	};

	return (
		<div className="slider-container text-center px-4">
			<Slider {...settings}>
				{Array.from(projects.values()).map((project) => (
					<div
						key={project.id}
						className="p-6 border rounded-lg shadow m-6 dark: bg-gradient-to-t  from-slate-900 to-slate-950 text-slate-800 dark:text-white space-y-4"
					>
						<h3 className="text-2xl font-bold">{project.title}</h3>
						<img
							className="
								rounded-t-lg
								w-full
								object-cover
								max-h-96
								md:max-h-96
							"
							src={
								project.images.length > 0
									? project.images[0].image
									: "placeholder-image-url"
							}
							alt={project.title || "Project image"}
						/>
						<p>{project.description}</p>
						<strong>Role: {project.contributionRole}</strong>
						<div className="flex overflow-x-auto pb-2 space-x-2">
							{project.tags.map((tag) => (
								<span
									key={tag}
									className="bg-blue-200 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded whitespace-nowrap"
								>
									{tag}
								</span>
							))}
						</div>
						{project.repoLink && (
							<a
								href={project.repoLink}
								target="_blank"
								rel="noopener noreferrer"
								className="inline-flex items-center px-3 py-2 bg-blue-700 rounded-lg text-white hover:bg-blue-800"
							>
								View on GitHub
							</a>
						)}
					</div>
				))}
			</Slider>
		</div>
	);
}
