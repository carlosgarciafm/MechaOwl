import disnake
from disnake.ext import commands


class RoleCommand(commands.Cog):
    """Manage user's current roles in the server."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def role(self, inter: disnake.CommandInteraction):
        """Manage user's current roles in the server."""
        pass

    @role.sub_command()
    async def list(
            self,
            inter: disnake.CommandInteraction,
            member: disnake.Member | None = None,
            public: bool = False,
            ):
        """List server-specific roles for the user.
        Parameters
        ---------------
        member: server member to query
        public: do you want to message to be visible by everyone?
        """
        if not isinstance(inter.author, disnake.Member):
            return await inter.response.send_message("You're not one of us.")

        member = member or inter.author
        description = f"***{member.name}'s roles are:\n***"
        for role in member.roles:
            description += f"{role.name}\n"
        embed = disnake.Embed(title="", description=description)
        await inter.response.send_message(embed=embed, ephemeral=public)

    @role.sub_command()
    async def assign(
            self,
            inter: disnake.CommandInteraction,
            role: disnake.Role
            ):
        """Self assign an existing role.
        Parameters
        ---------------
        role: which role do you want?
        """
        if not isinstance(inter.author, disnake.Member):
            return await inter.response.send_message("You're not one of us.")

        if inter.author.bot:
            return await inter.response.send_message("Access denied for bots.")
        if role._permissions > inter.author.guild_permissions.value:
            return await inter.response.send_message(
            "You don't have the privileges to be assigned this role.")

        await inter.author.add_roles(role)
        await inter.response.send_message(f"You were assigned the role of {role}.")

    @role.sub_command()
    async def revoke(
            self,
            inter: disnake.CommandInteraction,
            role: disnake.Role
            ):
        """Self remove role from member.
        Parameters
        ---------------
        role: which role do you want to remove?
        """
        if not isinstance(inter.author, disnake.Member):
            return await inter.response.send_message("You're not one of us.")

        if inter.author.bot:
            return await inter.response.send_message("Access denied for bots.")

        if role not in inter.author.roles:
            return await inter.response.send_message(f"You don't currently have the {role} role assigned.")
        await inter.author.remove_roles(role)
        await inter.response.send_message(f"You were removed the role of {role}.")

    @role.sub_command()
    async def create(
            self,
            inter: disnake.CommandInteraction,
            name: str,
            colour: disnake.Colour,
            ):
        """Create a new role for the server.
        Parameters
        ---------------
        name: what's the name for the new role?
        colour: what's the colour for the new role? (hex format #f00 #ff0000)
        """
        if not isinstance(inter.guild, disnake.Guild):
            return await inter.response.send_message("Invalid server.")
        for role in inter.guild.roles:
            if name.lower() == role.name.lower():
                return await inter.response.send_message("Role already exists.")

        await inter.guild.create_role(name=name, colour=colour)
        await inter.response.send_message(f"Created new role {name}.")

    @role.sub_command()
    async def delete(
            self,
            inter: disnake.CommandInteraction,
            role: disnake.Role,
            ):
        """Delete an existing role in the server.
        Parameters
        ---------------
        name: which role do you want to delete?
        """
        if not isinstance(inter.author, disnake.Member):
            return await inter.response.send_message("You're not one of us.")

        if not isinstance(inter.guild, disnake.Guild):
            return await inter.response.send_message("Invalid server.")
        if role not in inter.guild.roles:
            return await inter.response.send_message("Role doesn't exist.")
        try:
            await role.delete()
            await inter.response.send_message(f"The role {role} has been deleted.")
        except disnake.Forbidden:
            await inter.response.send_message("You don't have the privileges to delete this role.")


def setup(bot: commands.Bot):
    bot.add_cog(RoleCommand(bot))
