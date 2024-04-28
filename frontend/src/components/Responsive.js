import React, { useState, useEffect, Suspense } from "react";
import axios from "axios";
import { capitalize } from "../utils/utils";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// Lazy import for Slider
const Slider = React.lazy(() => import("react-slick"));

const Responsive = () => {
	const [projects, setProjects] = useState([]);
	const [isLoading, setIsLoading] = useState(true);

	useEffect(() => {
		const fetchProjects = async () => {
			setIsLoading(true);
			try {
				const response = await axios.get("http://localhost:8000/api/projects/");
				setProjects(response.data);
			} catch (error) {
				console.error("There was an error fetching the projects:", error);
			} finally {
				setIsLoading(false);
			}
		};

		fetchProjects();
	}, []);

	var settings = {
		dots: true,
		infinite: true,
		speed: 500,
		slidesToShow: 1, // Set to 1 for better readability
		slidesToScroll: 1,
		initialSlide: 0,
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					infinite: true,
					dots: true,
				},
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					initialSlide: 2,
				},
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				},
			},
		],
	};

	return (
		<div className="slider-container container mx-auto p-10">
			{isLoading ? (
				<p>Loading...</p>
			) : (
				<Suspense fallback={<div>Loading Slider...</div>}>
					<Slider {...settings}>
						{projects.map((project) => (
							<div key={project.id} className="text-center p-10">
								<h3>{capitalize(project.title)}</h3>
								<p>{project.description}</p>
								<div>
									<strong>Role:</strong>{" "}
									{project.contribution_role || "Not specified"}
								</div>
								<div>
									<strong>Technologies:</strong>{" "}
									{project.technologies || "Not specified"}
								</div>
								<div>
									<strong>Tags:</strong> {project.tags.join(", ")}
								</div>
								{project.images && project.images.length > 0 && (
									<img
										src={project.images[0].image}
										alt={project.images[0].caption || "Project thumbnail"}
										className="w-full object-scale-down"
										style={{ height: "600px" }}
									/>
								)}
								{project.repo_link && (
									<a
										href={project.repo_link}
										target="_blank"
										rel="noopener noreferrer"
									>
										View on GitHub
									</a>
								)}
								{project.link && (
									<a
										href={project.link}
										target="_blank"
										rel="noopener noreferrer"
									>
										View Project
									</a>
								)}
							</div>
						))}
					</Slider>
				</Suspense>
			)}
		</div>
	);
};

export default Responsive;
