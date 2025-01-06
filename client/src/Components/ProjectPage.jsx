import ProjectCard from "./ProjectCard/ProjectCard";
const ProjectPage = () => {
  return (
    <main className="ProjectCardList">
      <ProjectCard
        title="Rock, Paper, Scissors"
        description="My first project! Enjoy!"
        language="HTML, CSS, JS"
      ></ProjectCard>
      <ProjectCard></ProjectCard>
    </main>
  );
};

export default ProjectPage;
