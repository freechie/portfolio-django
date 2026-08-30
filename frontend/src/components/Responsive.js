import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

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
    detail_url,
  }) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.contributionRole = contribution_role;
    this.createdAt = created_at;
    this.updatedAt = updated_at;
    this.status = status;
    this.technologies = technologies;
    this.tags = tags || [];
    this.images = images || [];
    this.repoLink = repo_link;
    this.isFeatured = is_featured;
    this.link = link;
    this.detailUrl = detail_url;
  }
}

export default function ProjectScroller() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("/api/projects/")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Project request failed with ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setProjects(data.map((projectData) => new Project(projectData)));
      })
      .catch(() => setError("Projects could not be loaded. Please try again."))
      .finally(() => setLoading(false));
  }, []);

  function CustomNextArrow(props) {
    const { className, style, onClick } = props;
    return (
      <button
        type="button"
        aria-label="Next project"
        className={className}
        style={{
          ...style,
          display: "block",
          right: "1px",
          background: "#18181B",
          color: "white",
          borderRadius: "30%",
        }}
        onClick={onClick}
      />
    );
  }

  function CustomPrevArrow(props) {
    const { className, style, onClick } = props;
    return (
      <button
        type="button"
        aria-label="Previous project"
        className={className}
        style={{
          ...style,
          display: "block",
          left: "25px",
          background: "#18181B",
          color: "white",
          borderRadius: "30%",
        }}
        onClick={onClick}
      />
    );
  }

  var settings = {
    initialSlide: 0,
    dots: false,
    lazyLoad: true,
    infinite: projects.length > 1,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: !window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    autoplaySpeed: 2000,
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

  if (loading) {
    return <p role="status">Loading projects...</p>;
  }

  if (error) {
    return <p role="alert">{error}</p>;
  }

  if (projects.length === 0) {
    return <p>No projects are available yet.</p>;
  }

  return (
    <div className="slider-container text-center px-4 py-2">
      <Slider {...settings}>
        {projects.map((project) => (
          <div
            key={project.id}
            className="p-8 rounded-lg shadow-lg mx-4 my-6 bg-gradient-to-t from-transparent to-neutral-100 dark:bg-gradient-to-b dark:from-transparent dark:to-inherit text-slate-700 dark:text-neutral-50 backdrop-filter backdrop-blur-lg"
          >
            <h3 className="text-4xl mb-10 font-semibold font-montserrat">
              <a href={project.detailUrl}>{project.title}</a>
            </h3>
            {project.images.length > 0 ? (
              <img
                className="rounded-lg w-full object-cover max-h-96 md:max-h-96 mb-8"
                src={project.images[0].image}
                alt={project.images[0].caption || `${project.title} preview`}
              />
            ) : (
              <p className="mb-8">No project preview is available.</p>
            )}
            <p className="mb-3 text-xl font-sans">{project.description}</p>
            <p className="mb-6 block text-lg font-semibold">
              Role: {project.contributionRole}
            </p>
            <div className="flex justify-center flex-wrap gap-3 my-3 overflow-x-auto">
              {project.tags.map((tag) => (
                <a
                  key={tag}
                  href={`/projects/tag/${encodeURIComponent(tag)}/`}
                  className=" bg-gradient-to-r from-indigo-600 to-indigo-900 text-neutral-200 text-md font-semibold px-3 py-1.5 rounded-full"
                >
                  {tag}
                </a>
              ))}
            </div>
            {project.repoLink && (
              <a
                href={project.repoLink}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center justify-center px-4 py-2 bg-gradient-to-r from-celestialblue-400 to-celestialblue-600 rounded-lg text-neutral-200 mt-4"
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
